%global packname  xtermStyle
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.2.1
Release:          1%{?dist}
Summary:          Basic text formatting using xterm escape sequences

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Text formatting in xterm and ansi terminals using escape sequences.
Supports colors and various font styles. It began as a standalone version
of the 'xterm256' package by Romain Francois since that package is tangled
up with the syntax highlighting package 'highlight' but has been developed
in another direction since then.  For some more sophisticated examples of
this package functionality check out the 'dataview' package as that was
the very reason 'xtermStyle' came into existence. However as 'xtermStyle'
can be used independently they were released separately.

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
%doc %{rlibdir}/xtermStyle/DESCRIPTION
%doc %{rlibdir}/xtermStyle/html
%{rlibdir}/xtermStyle/NAMESPACE
%{rlibdir}/xtermStyle/help
%{rlibdir}/xtermStyle/R
%{rlibdir}/xtermStyle/INDEX
%{rlibdir}/xtermStyle/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.1-1
- initial package for Fedora