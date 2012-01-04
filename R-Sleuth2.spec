%global packname  Sleuth2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Data sets from Ramsey and Schafer's "Statistical Sleuth (2nd ed)"

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Data sets from Ramsey, F.L. and Schafer, D.W. (2002), "The Statistical
Sleuth: A Course in Methods of Data Analysis (2nd ed)" Duxbury.

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
%doc %{rlibdir}/Sleuth2/DESCRIPTION
%doc %{rlibdir}/Sleuth2/doc
%doc %{rlibdir}/Sleuth2/html
%{rlibdir}/Sleuth2/NAMESPACE
%{rlibdir}/Sleuth2/Meta
%{rlibdir}/Sleuth2/R
%{rlibdir}/Sleuth2/data
%{rlibdir}/Sleuth2/INDEX
RPM build errors:
%{rlibdir}/Sleuth2/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.4-1
- initial package for Fedora