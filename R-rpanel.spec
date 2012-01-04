%global packname  rpanel
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Simple Interactive Controls for R Using the tcltk Package.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk 

BuildRequires:    R-devel tex(latex) R-tcltk 

%description
rpanel provides a set of functions to build simple GUI controls for R
functions.  These are built on the tcltk package. Uses could include
changing a parameter on a graph by animating it with a slider or a
"doublebutton", up to more sophisticated control panels.

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
%doc %{rlibdir}/rpanel/DESCRIPTION
%doc %{rlibdir}/rpanel/html
%doc %{rlibdir}/rpanel/CITATION
%doc %{rlibdir}/rpanel/COPYING
%{rlibdir}/rpanel/demo
%{rlibdir}/rpanel/R
%{rlibdir}/rpanel/help
%{rlibdir}/rpanel/history.txt
%{rlibdir}/rpanel/data
%{rlibdir}/rpanel/Meta
%{rlibdir}/rpanel/NAMESPACE
%{rlibdir}/rpanel/INDEX
%{rlibdir}/rpanel/images

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.6-1
- initial package for Fedora