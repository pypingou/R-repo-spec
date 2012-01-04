%global packname  PBSmodelling
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.63.229
Release:          1%{?dist}
Summary:          GUI Tools Made Easy: Interact with Models, Explore Data, Give Dynamic Presentations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
PBS Modelling provides software to facilitate the design, testing, and
operation of computer models. It focuses particularly on tools that make
it easy to construct and edit a customized graphical user interface (GUI).
Although it depends heavily on the R interface to the Tcl/Tk package, a
user does not need to know Tcl/Tk. The package contains examples that
illustrate models built with other R packages, including PBSmapping,
deSolve, PBSddesolve, and BRugs. It also serves as a convenient prototype
for building new R packages, along with instructions and batch files to
facilitate that process. The R directory '.../library/PBSmodelling/doc'
includes a complete user guide PBSmodelling-UG.pdf. To use this package
effectively, please consult the guide.

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
%doc %{rlibdir}/PBSmodelling/doc
%doc %{rlibdir}/PBSmodelling/DESCRIPTION
%doc %{rlibdir}/PBSmodelling/html
%{rlibdir}/PBSmodelling/unitTests
%{rlibdir}/PBSmodelling/help
%{rlibdir}/PBSmodelling/libs
%{rlibdir}/PBSmodelling/Meta
%{rlibdir}/PBSmodelling/PBStools
%{rlibdir}/PBSmodelling/NAMESPACE
%{rlibdir}/PBSmodelling/thirdparty
%{rlibdir}/PBSmodelling/examples
%{rlibdir}/PBSmodelling/tcl_scripts
%{rlibdir}/PBSmodelling/INDEX
%{rlibdir}/PBSmodelling/testWidgets
RPM build errors:
%{rlibdir}/PBSmodelling/win
%{rlibdir}/PBSmodelling/data
%{rlibdir}/PBSmodelling/demo
%{rlibdir}/PBSmodelling/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.63.229-1
- initial package for Fedora