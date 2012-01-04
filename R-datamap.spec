%global packname  datamap
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          A system for mapping foreign objects to R variables and environments

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-DBI 

BuildRequires:    R-devel tex(latex) R-DBI 

%description
datamap utilizes variable bindings and objects of class
"UserDefinedDatabase" to provide a simple mapping system to foreign
objects. Maps can be used as environments or attached to the search path,
and changes to either are persistent. Mapped foreign objects are fetched
in real-time and are never cached by the mapping system.

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
%doc %{rlibdir}/datamap/html
%doc %{rlibdir}/datamap/DESCRIPTION
%{rlibdir}/datamap/R
%{rlibdir}/datamap/help
%{rlibdir}/datamap/INDEX
%{rlibdir}/datamap/libs
%{rlibdir}/datamap/NAMESPACE
%{rlibdir}/datamap/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora