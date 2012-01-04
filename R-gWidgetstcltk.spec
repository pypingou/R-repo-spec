%global packname  gWidgetstcltk
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.48
Release:          1%{?dist}
Summary:          Toolkit implementation of gWidgets for tcltk package

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-48.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-gWidgets R-tcltk R-tcltk2 R-digest 


BuildRequires:    R-devel tex(latex) R-methods R-gWidgets R-tcltk R-tcltk2 R-digest



%description
Port of the gWidgets API to the tcltk package. Requires TK 8.5 or greater
for the tile (ttk)widgets http://www.tcl.tk/software/tcltk/8.5.tml. This
is the default on Windows. Under linux, Tk must be installed. Under Mac OS
X (10.5) there are two options: native Tk or X11. For the native one, Tk
must be upgraded. See www.tcl.tk to download source. Under the Mac it
compiles and installs cleanly. For X11, tcltk libraries can be downloaded
to augment the R binary package. See
http://cran.r-project.org/bin/macosx/tools/. The gdf function requires the
add on Tk package TkTable (http://tktable.sourceforge.net/).

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.48-1
- initial package for Fedora