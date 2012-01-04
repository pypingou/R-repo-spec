%global packname  bsml
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.0
Release:          1%{?dist}
Summary:          Basis Selection from Multiple Libraries

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.5-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
BSML stands for Basis Selection from Multiple Libraries and it is a
methodology for spatially-adaptive multivariate regression. To fit a
nonparametric or semiparametric regression model, multiple libraries may
be used to approximate the mean function. The program will adaptively
select basis functions from each library and find the optimal model
complexity by using the Generalized Degrees of Freedom or Covariance

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.0-1
- initial package for Fedora