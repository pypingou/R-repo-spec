%global packname  BiomarkeR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Paired (pBI) and Unpaired Biomarker Identifier (uBI) including a method to infer networks.

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-igraph R-Hmisc 


BuildRequires:    R-devel tex(latex) R-igraph R-Hmisc



%description
This package allows to rank features and infer networks based on the
Paired (pBI) and Unpaired Biomarker Identifier (uBI).

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
%doc %{rlibdir}/BiomarkeR/DESCRIPTION
%doc %{rlibdir}/BiomarkeR/doc
%doc %{rlibdir}/BiomarkeR/html
%{rlibdir}/BiomarkeR/data
%{rlibdir}/BiomarkeR/R
%{rlibdir}/BiomarkeR/INDEX
%{rlibdir}/BiomarkeR/help
%{rlibdir}/BiomarkeR/Meta
%{rlibdir}/BiomarkeR/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora