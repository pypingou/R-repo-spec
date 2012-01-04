%global packname  RcmdrPlugin.DoE
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.11.5
Release:          1%{?dist}
Summary:          R Commander Plugin for (industrial) Design of Experiments

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.11-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk R-DoE.base R-FrF2 R-DoE.wrapper R-Rcmdr 

BuildRequires:    R-devel tex(latex) R-tcltk R-DoE.base R-FrF2 R-DoE.wrapper R-Rcmdr 

%description
WARNING: This package is currently in beta status! The package provides a
platform-independent GUI for design of experiments. It is implemented as a
plugin to the R-Commander, which is a more general graphical user
interface for statistics in R based on tcl/tk. DoE functionality can be
accessed through the menu Design that is added to the R-Commander menus.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.11.5-1
- initial package for Fedora