%global packname  dataview
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Human readable data presentation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-xtermStyle 

BuildRequires:    R-devel tex(latex) R-xtermStyle 

%description
This package provides clear, informative and colorfull ways of presenting
the contents of data.frame, list, environment etc. in the prompt.  Ideally
this package should be used in terminals supporting xterm 256 colour mode,
e.g. the standard Ubuntu terminal. The Mac OS X terminal (as of Snow
Leopard) only support ANSI colour, which still works but doesn't look as
nice. On Windows systems no colouring is supported.  If the output of
functions like 'whos' is a mess or somehow doesn't look like it should
check the help for the functions 'style' and 'style.mode' of the
'xtermStyle' package.

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
%doc %{rlibdir}/dataview/html
%doc %{rlibdir}/dataview/DESCRIPTION
%{rlibdir}/dataview/Meta
%{rlibdir}/dataview/INDEX
%{rlibdir}/dataview/R
%{rlibdir}/dataview/NAMESPACE
%{rlibdir}/dataview/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.1-1
- initial package for Fedora