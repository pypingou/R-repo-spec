%global packname  rvmbinary
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          RVM-Classification and Regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-kernlab 

BuildRequires:    R-devel tex(latex) R-kernlab 

%description
Performs binary classification and regression of data using a Relevance
Vector Machine

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
%doc %{rlibdir}/rvmbinary/html
%doc %{rlibdir}/rvmbinary/DESCRIPTION
%{rlibdir}/rvmbinary/help
%{rlibdir}/rvmbinary/INDEX
%{rlibdir}/rvmbinary/NAMESPACE
%{rlibdir}/rvmbinary/R
%{rlibdir}/rvmbinary/libs
%{rlibdir}/rvmbinary/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora