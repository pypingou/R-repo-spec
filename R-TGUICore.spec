%global packname  TGUICore
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.15
Release:          1%{?dist}
Summary:          Teaching GUI - Core functionality

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk R-tkrplot R-utils 

BuildRequires:    R-devel tex(latex) R-tcltk R-tkrplot R-utils 

%description
Teaching GUI (A Graphical User Interface to enhance and support modern
teaching methods in an interactive way.) - basic framework. Providing a
student and a trainer interface, containing all facilities needed to
create interactive examples, checks or ask for student feedback.

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
%doc %{rlibdir}/TGUICore/doc
%doc %{rlibdir}/TGUICore/CITATION
%doc %{rlibdir}/TGUICore/DESCRIPTION
%doc %{rlibdir}/TGUICore/html
%{rlibdir}/TGUICore/NAMESPACE
%{rlibdir}/TGUICore/Meta
%{rlibdir}/TGUICore/etc
%{rlibdir}/TGUICore/INDEX
%{rlibdir}/TGUICore/R
%{rlibdir}/TGUICore/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.15-1
- initial package for Fedora