%global packname  popPK
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.03
Release:          1%{?dist}
Summary:          Summary of Population Pharmacokinetic Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Hmisc R-lattice R-grid R-xpose4 

BuildRequires:    R-devel tex(latex) R-Hmisc R-lattice R-grid R-xpose4 

%description
This package uses xpose4 to create standard graphs and tables for NONMEM

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
%doc %{rlibdir}/popPK/html
%doc %{rlibdir}/popPK/DESCRIPTION
%{rlibdir}/popPK/Meta
%{rlibdir}/popPK/INDEX
%{rlibdir}/popPK/NAMESPACE
%{rlibdir}/popPK/extdata
%{rlibdir}/popPK/R
%{rlibdir}/popPK/help

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.03-1
- initial package for Fedora