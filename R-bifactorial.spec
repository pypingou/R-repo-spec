%global packname  bifactorial
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.6
Release:          1%{?dist}
Summary:          Inferences for bi- and trifactorial trial designs

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm R-multcomp R-lattice R-graphics R-methods R-Rcpp 


BuildRequires:    R-devel tex(latex) R-mvtnorm R-multcomp R-lattice R-graphics R-methods R-Rcpp



%description
This package makes global and multiple inferences for given bi- and
trifactorial clinical trial designs using bootstrap methods and a
classical approach.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.6-1
- initial package for Fedora