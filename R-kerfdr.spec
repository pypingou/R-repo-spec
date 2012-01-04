%global packname  kerfdr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          semi-parametric kernel-based approach to local fdr estimations

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
semi-parametric kernel-based approaches to local fdr estimations useful
for the testing of multiple hypothesis (in large-scale genetic, genomic
and post-genomic studies for instance).

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
%doc %{rlibdir}/kerfdr/DESCRIPTION
%doc %{rlibdir}/kerfdr/html
%{rlibdir}/kerfdr/NAMESPACE
%{rlibdir}/kerfdr/R
%{rlibdir}/kerfdr/Meta
%{rlibdir}/kerfdr/help
%{rlibdir}/kerfdr/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.1-1
- initial package for Fedora