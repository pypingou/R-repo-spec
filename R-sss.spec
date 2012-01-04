%global packname  sss
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.08
Release:          1%{?dist}
Summary:          Tools for importing files in the triple-s .(Standard Survey Structure) format

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-08.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 
Requires:         R-plyr R-XML 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-plyr R-XML 


%description
sss is a set of tools to import survey files in the .sss (triple-s)
format. It provides the function read.sss that reads the .asc and .sss
files of a triple-s survey data file.  The package is experimental -
feedback, issues and bug reports are welcome.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.08-1
- initial package for Fedora