%global packname  R.oo
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.3
Release:          1%{?dist}
Summary:          R object-oriented programming with or without references

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-R.methodsS3 R-utils 

BuildRequires:    R-devel tex(latex) R-R.methodsS3 R-utils 

%description
Methods and classes for object-oriented programming in R with or without
references.  Large effort has been made on making definition of methods as
simple as possible with a minimum of maintenance for package developers. 
The package has been developed since 2001 and is now considered very
stable.  This is a cross-platform package implemented in pure R that
defines standard S3 classes without any tricks.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.3-1
- initial package for Fedora