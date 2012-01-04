%global packname  RcmdrPlugin.pointG
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Rcmdr Graphical POINT of view for questionnaire data Plug-In

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Rcmdr R-tcltk R-MASS R-lattice R-qgraph R-VIM R-maps R-YaleToolkit R-ade4 R-effects R-RColorBrewer R-Hmisc R-car 


BuildRequires:    R-devel tex(latex) R-Rcmdr R-tcltk R-MASS R-lattice R-qgraph R-VIM R-maps R-YaleToolkit R-ade4 R-effects R-RColorBrewer R-Hmisc R-car



%description
This package provides an Rcmdr "plug-in" to analyze questionnaire data.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora