%global packname  GPseq
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          gpseq: Using the generalized Poisson distribution to model sequence read counts from high throughput sequencing experiments

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Some functions for modeling sequence read counts as a generalized poisson
model and to use this model for detecting differentially expressed genes
in different conditions and differentially spliced exons.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/GPseq/html
%doc %{rlibdir}/GPseq/DESCRIPTION
%{rlibdir}/GPseq/help
%{rlibdir}/GPseq/INDEX
%{rlibdir}/GPseq/data
%{rlibdir}/GPseq/Meta
%{rlibdir}/GPseq/NAMESPACE
%{rlibdir}/GPseq/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5-1
- initial package for Fedora