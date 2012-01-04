%global packname  RcmdrPlugin.TextMining
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Rcommander plugin for "tm" package

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk R-tm R-XML R-Snowball R-Rgraphviz R-proxy R-Rcmdr 


BuildRequires:    R-devel tex(latex) R-tcltk R-tm R-XML R-Snowball R-Rgraphviz R-proxy R-Rcmdr



%description
WARNING: This package is currently in beta status! This package provide
GUI for demonstration of text mining concepts and "tm" package. It is
implemented as a plugin to the R-Commander, which is based on tcl/tk. This
set of dialogs can be accessed through the menu TextMining that is added
to the R-Commander menus.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0-1
- initial package for Fedora