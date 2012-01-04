%global packname  relax
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.7
Release:          1%{?dist}
Summary:          relax -- R Editor for Literate Analysis and lateX

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk 

BuildRequires:    R-devel tex(latex) R-tcltk 

%description
package relax contains some functions for report writing, presentation,
and programming: relax(), tangleR(), weaveR(), (g)slider(). "relax" is
written in R and Tcl/Tk. relax creates a new window (top level Tcl/Tk
widget) that consists of two text fields and some buttons and menus. Text
(chunks) and code (chunks) are inserted in the upper text field (report
field). Code chunks are evaluated by clicking on EvalRCode. Results are
shown in the lower text field (output field) and will be transfered to the
report field by pressing on Insert. In this way you get correct reports.
These reports can be loaded again in cause of presentation, modification
and result checking. tangleR() and weaveR() implement a plain kind of
tangling and weaving. gslider() and slider() are designed to define
sliders for interactive experiments in a simple way. The syntax rules of
code chunks and text chunks are defined by the noweb system proposed by
Norman Ramsey (http://www.eecs.harvard.edu/~nr/noweb/intro.html). For
integrating jpeg graphics into the text field you need the Tcl/Tk Img
package of Jan Nijtmans (see:
http://members.chello.nl/~j.nijtmans/img.html,
http://home.kpnplanet.nl/~J.Nijtmans@kpnplanet.nl/img.html or
http://tkimg.sourceforge.net/, the package is found on
http://sourceforge.net/projects/tkimg). If an Img version is integrated in
the relax package the license terms concerning the img package will be
found in the source file of the package, for example in:
relax/src/tkimg1.3.tar.gz. Older windows versions of relax contain the
Tcl/Tk img package, so no further installations have to be done.

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
%doc %{rlibdir}/relax/html
%doc %{rlibdir}/relax/DESCRIPTION
%{rlibdir}/relax/src
%{rlibdir}/relax/help
%{rlibdir}/relax/INDEX
%{rlibdir}/relax/NAMESPACE
%{rlibdir}/relax/lib
%{rlibdir}/relax/config
%{rlibdir}/relax/Meta
%{rlibdir}/relax/rev
%{rlibdir}/relax/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.7-1
- initial package for Fedora