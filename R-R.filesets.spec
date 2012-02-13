%global packname  R.filesets
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.4
Release:          1%{dist}
Summary:          Easy handling of and access to files organized in structured directories

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-R.methodsS3 R-R.oo R-R.utils R-digest 

BuildRequires:    R-devel tex(latex) R-R.methodsS3 R-R.oo R-R.utils R-digest 

%description
A file set refers to a set of files located in one or more directories on
the file system.  This package provides classes and methods to locate,
setup, subset, navigate and iterate suchs sets.  The API is designed such
that these classes can be subsetted to provide a richer API for special
file formats.  Moreover, a specific name format is defined such that
filenames and directories can be considered to have fullnames which
consists of a name followed by comma-separated tags.  This adds additional
flexibility to identify file sets and individual files.  NOTE: This
package's API should be considered to be in an beta stage.  Its main
purpose is currently to support the aroma.* packages, where it is one of
the main core components; if you decide to build on top of this package,
please contact the author first.

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
%doc %{rlibdir}/R.filesets/DESCRIPTION
%doc %{rlibdir}/R.filesets/NEWS
%doc %{rlibdir}/R.filesets/html
%{rlibdir}/R.filesets/R
%{rlibdir}/R.filesets/exData
%{rlibdir}/R.filesets/Meta
%{rlibdir}/R.filesets/NAMESPACE
%{rlibdir}/R.filesets/help
%{rlibdir}/R.filesets/INDEX

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.4-1
- Update to version 1.1.4

* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.3-1
- initial package for Fedora