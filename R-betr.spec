%global packname  betr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.10.0
Release:          1%{?dist}
Summary:          Identify differentially expressed genes in microarray time-course data

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-Biobase R-limma R-mvtnorm R-methods R-stats 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-Biobase R-limma R-mvtnorm R-methods R-stats 


%description
The betr package implements the BETR (Bayesian Estimation of Temporal
Regulation) algorithm to identify differentially expressed genes in
microarray time-course data.

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
%doc %{rlibdir}/betr/doc
%doc %{rlibdir}/betr/html
%doc %{rlibdir}/betr/DESCRIPTION
%{rlibdir}/betr/R
%{rlibdir}/betr/data
%{rlibdir}/betr/INDEX
%{rlibdir}/betr/Meta
%{rlibdir}/betr/help
%{rlibdir}/betr/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10.0-1
- initial package for Fedora