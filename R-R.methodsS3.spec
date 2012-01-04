%global packname  R.methodsS3
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Utility function for defining S3 methods

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Methods that simplify the setup of S3 generic functions and S3 methods. 
Major effort has been made in making definition of methods as simple as
possible with a minimum of maintenance for package developers.  For
example, generic functions are created automatically, if missing, and
naming conflict are automatically solved, if possible.  The method
setMethodS3() is a good start for those who in the future want to migrate
to S4.  This is a cross-platform package implemented in pure R and
generates standard S3 methods.

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
%doc %{rlibdir}/R.methodsS3/CITATION
%doc %{rlibdir}/R.methodsS3/DESCRIPTION
%doc %{rlibdir}/R.methodsS3/html
%doc %{rlibdir}/R.methodsS3/NEWS
%{rlibdir}/R.methodsS3/R
%{rlibdir}/R.methodsS3/HOWTOCITE
%{rlibdir}/R.methodsS3/INDEX
%{rlibdir}/R.methodsS3/help
%{rlibdir}/R.methodsS3/NAMESPACE
%{rlibdir}/R.methodsS3/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora