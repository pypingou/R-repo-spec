%global packname  stepPlr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.92
Release:          1%{?dist}
Summary:          L2 penalized logistic regression with a stepwise variable selection

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
L2 penalized logistic regression for both continuous and discrete
predictors, with forward stagewise/forward stepwise variable selection

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
%doc %{rlibdir}/stepPlr/html
%doc %{rlibdir}/stepPlr/DESCRIPTION
%{rlibdir}/stepPlr/NAMESPACE
%{rlibdir}/stepPlr/Meta
%{rlibdir}/stepPlr/libs
%{rlibdir}/stepPlr/INDEX
%{rlibdir}/stepPlr/R
%{rlibdir}/stepPlr/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.92-1
- initial package for Fedora