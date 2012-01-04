%global packname  LogitNet
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Infer network based on binary arrays using regularized logistic regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
LogitNet is developed for inferring network of binary variables under the
high-dimension-low-sample-size setting

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
%doc %{rlibdir}/LogitNet/DESCRIPTION
%doc %{rlibdir}/LogitNet/html
%{rlibdir}/LogitNet/NAMESPACE
%{rlibdir}/LogitNet/help
%{rlibdir}/LogitNet/INDEX
%{rlibdir}/LogitNet/Meta
%{rlibdir}/LogitNet/data
%{rlibdir}/LogitNet/R
%{rlibdir}/LogitNet/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora