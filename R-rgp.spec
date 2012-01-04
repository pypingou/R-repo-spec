%global packname  rgp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          R genetic programming framework

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-emoa R-rrules 

BuildRequires:    R-devel tex(latex) R-methods R-emoa R-rrules 

%description
RGP is a simple modular Genetic Programming (GP) system build in pure R.
In addition to general GP tasks, the system supports Symbolic Regression
by GP through the familiar R model formula interface. GP individuals are
represented as R expressions, an (optional) type system enables
domain-specific function sets containing functions of diverse domain- and
range types. A basic set of genetic operators for variation (mutation and
crossover) and selection is provided.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.4-1
- initial package for Fedora