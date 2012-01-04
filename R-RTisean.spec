%global packname  RTisean
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.0.13
Release:          1%{?dist}
Summary:          R interface to Tisean algorithms

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-tcltk 

BuildRequires:    R-devel tex(latex) R-tcltk 

%description
Algorithms for time series analysis from nonlinear dynamical systems
theory originally made available by Rainer Hegger, Holger Kantz and Thomas
Schreiber at the site http://www.mpipks-dresden.mpg.de/~tisean/ .  A
related R package (tseriesChaos by Antonio, Fabio Di Narzo) contains
rewritten versions of a few of the TISEAN algorithms.  The intention of
the present package is to use the TISEAN routines from within R with no
need of manual importing/exporting.  It is in a beta version state, though
most of the functions should be usable.  Correspondence should be sent to
either Marji Lines, lines@dss.uniud.it, or to the current maintainer of
the package. This package only contains R interface code. It requires that
you have the Tisean-3.0.1 algorithms available on your computer.

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
%doc %{rlibdir}/RTisean/DESCRIPTION
%doc %{rlibdir}/RTisean/html
%{rlibdir}/RTisean/INDEX
%{rlibdir}/RTisean/Meta
%{rlibdir}/RTisean/R
%{rlibdir}/RTisean/NAMESPACE
%{rlibdir}/RTisean/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.0.13-1
- initial package for Fedora