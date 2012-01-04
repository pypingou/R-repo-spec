%global packname  qtlbim
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.9.4
Release:          1%{?dist}
Summary:          QTL Bayesian Interval Mapping

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-qtl R-lattice R-coda R-tools R-MASS 

BuildRequires:    R-devel tex(latex) R-stats R-qtl R-lattice R-coda R-tools R-MASS 

%description
Functions for model selection for genetic architecture.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.9.4-1
- initial package for Fedora