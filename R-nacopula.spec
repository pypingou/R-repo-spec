%global packname  nacopula
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.9.1
Release:          1%{?dist}
Summary:          Nested Archimedean Copulas

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-9-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-stats4 
Requires:         R-gsl R-ADGofTest R-stabledist 

BuildRequires:    R-devel tex(latex) R-methods R-stats4
BuildRequires:    R-gsl R-ADGofTest R-stabledist 


%description
An R package for working with nested Archimedean copulas. Specifically,
providing procedures for computing function values and cube volumes,
characteristics such as Kendall's tau and tail dependence coefficients,
efficient sampling algorithms, various estimators, and goodness-of-fit
tests.  The package also contains related univariate distributions and
special functions such as the Sibuya distribution, the polylogarithm,
Stirling and Eulerian numbers.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.9.1-1
- initial package for Fedora