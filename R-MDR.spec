%global packname  MDR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Detect gene-gene interactions using multifactor dimensionality reduction

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-lattice 

%description
Performs multifactor dimensionality reduction (MDR) to detect potential
gene-gene interactions in case-control studies.

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
%doc %{rlibdir}/MDR/DESCRIPTION
%doc %{rlibdir}/MDR/LICENCE
%doc %{rlibdir}/MDR/html
%{rlibdir}/MDR/Meta
%{rlibdir}/MDR/NAMESPACE
%{rlibdir}/MDR/R
%{rlibdir}/MDR/help
%{rlibdir}/MDR/data
%{rlibdir}/MDR/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora