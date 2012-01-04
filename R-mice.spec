%global packname  mice
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.10
Release:          1%{?dist}
Summary:          Multivariate Imputation by Chained Equations

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-nnet R-methods R-lattice R-stringr 

BuildRequires:    R-devel tex(latex) R-MASS R-nnet R-methods R-lattice R-stringr 

%description
Multiple Imputation using Fully Conditional Specification

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
%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.10-1
- initial package for Fedora