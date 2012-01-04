%global packname  gWidgetsWWW
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.22
Release:          1%{?dist}
Summary:          Toolkit implementation of the gWidgets API for use with web pages

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-22.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-proto R-filehash R-digest R-rjson 


BuildRequires:    R-devel tex(latex) R-methods R-proto R-filehash R-digest R-rjson



%description
Port of the gWidgets API to program dynamic websites. Can be used with R's
dynamic help web server to serve local files. This provides a convenient
means to make local GUIs for users without concern for external GUI
toolkits. Also, in combination with RApache,
http://biostat.mc.vanderbilt.edu/rapache/index.html, this framework can be
used to make public websites powered by R. The Ext JavaScript libararies
(www.extjs.com) are used to create and manipulate the widgets dynamically.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.22-1
- initial package for Fedora