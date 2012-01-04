%global packname  mvnmle
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.10
Release:          1%{?dist}
Summary:          ML estimation for multivariate normal data with missing values.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Finds the maximum likelihood estimate of the mean vector and
variance-covariance matrix for multivariate normal data with missing

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
%doc %{rlibdir}/mvnmle/DESCRIPTION
%doc %{rlibdir}/mvnmle/html
%{rlibdir}/mvnmle/data
%{rlibdir}/mvnmle/help
%{rlibdir}/mvnmle/Meta
%{rlibdir}/mvnmle/INDEX
%{rlibdir}/mvnmle/R
%{rlibdir}/mvnmle/libs
RPM build errors:
%{rlibdir}/mvnmle/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.10-1
- initial package for Fedora