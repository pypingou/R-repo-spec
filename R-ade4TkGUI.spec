%global packname  ade4TkGUI
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.5
Release:          1%{?dist}
Summary:          ade4 Tcl/Tk Graphical User Interface

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-ade4 R-tcltk 


BuildRequires:    R-devel tex(latex) R-ade4 R-tcltk



%description
a Tcl/Tk GUI for some basic functions in the ade4 package

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.5-1
- initial package for Fedora