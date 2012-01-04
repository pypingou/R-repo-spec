%global packname  Mangrove
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Risk prediction on trees

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Mangrove is an R package for performing genetic risk prediction from
genotype data.  You can use it to perform risk prediction for individuals,
or for families with missing data.

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
%doc %{rlibdir}/Mangrove/html
%doc %{rlibdir}/Mangrove/DESCRIPTION
%doc %{rlibdir}/Mangrove/doc
%{rlibdir}/Mangrove/Meta
%{rlibdir}/Mangrove/data
%{rlibdir}/Mangrove/LICENSE
%{rlibdir}/Mangrove/R
%{rlibdir}/Mangrove/NAMESPACE
%{rlibdir}/Mangrove/help
%{rlibdir}/Mangrove/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora