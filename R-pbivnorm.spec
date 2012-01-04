%global packname  pbivnorm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Vectorized Bivariate Normal CDF

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Provides a vectorized R function for calculating probabilities from a
standard bivariate normal CDF.

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
%doc %{rlibdir}/pbivnorm/DESCRIPTION
%doc %{rlibdir}/pbivnorm/html
%doc %{rlibdir}/pbivnorm/NEWS
%{rlibdir}/pbivnorm/Meta
%{rlibdir}/pbivnorm/libs
%{rlibdir}/pbivnorm/R
%{rlibdir}/pbivnorm/NAMESPACE
%{rlibdir}/pbivnorm/help
%{rlibdir}/pbivnorm/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.0-1
- initial package for Fedora