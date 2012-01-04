%global packname  rysgran
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Grain size analysis, textural classifications and distribution of unconsolidated sediments

Group:            Applications/Engineering 
License:          GPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-soiltexture R-lattice 


BuildRequires:    R-devel tex(latex) R-soiltexture R-lattice



%description
This package is a port to R of the SysGran program, written in Delphi by
Camargo (2006). It contains functions for the analysis of grain size
samples (only in phi scale in this version) based on various methods, like
Folk & Ward (1957) and Methods of Moments (Tanner, 1995), among others;
textural classifications and distribution of unconsolidated sediments are
shown in histograms, bivariated plots and ternary diagrams of Shepard
(1954) and Pejrup (1988). English and Portuguese languages are supported
in outputs

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
%doc %{rlibdir}/rysgran/DESCRIPTION
%doc %{rlibdir}/rysgran/html
%{rlibdir}/rysgran/data
%{rlibdir}/rysgran/NAMESPACE
%{rlibdir}/rysgran/INDEX
%{rlibdir}/rysgran/R
%{rlibdir}/rysgran/Meta
%{rlibdir}/rysgran/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora