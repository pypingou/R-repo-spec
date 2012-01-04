%global packname  RSQLite.extfuns
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Math and String Extension Functions for RSQLite

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-RSQLite 

BuildRequires:    R-devel tex(latex) R-RSQLite 

%description
This package uses SQLite's loadable extension feature to provide a number
of additional SQL functions and aggregates. The package is a wrapper of
extension functions written by Liam Healy and made available through the
SQLite website (http://www.sqlite.org/contrib).  Math: acos, asin, atan,
atn2, atan2, acosh, asinh, atanh, difference, degrees, radians, cos, sin,
tan, cot, cosh, sinh, tanh, coth, exp, log, log10, power, sign, sqrt,
square, ceil, floor, pi. String: replicate, charindex, leftstr, rightstr,
ltrim, rtrim, trim, replace, reverse, proper, padl, padr, padc, strfilter.
Aggregate: stdev, variance, mode, median, lower_quartile, upper_quartile.

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
%doc %{rlibdir}/RSQLite.extfuns/html
%doc %{rlibdir}/RSQLite.extfuns/DESCRIPTION
%{rlibdir}/RSQLite.extfuns/NAMESPACE
%{rlibdir}/RSQLite.extfuns/help
%{rlibdir}/RSQLite.extfuns/Meta
%{rlibdir}/RSQLite.extfuns/INDEX
%{rlibdir}/RSQLite.extfuns/R
%{rlibdir}/RSQLite.extfuns/libs

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.1-1
- initial package for Fedora