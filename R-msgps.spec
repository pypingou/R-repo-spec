%global packname  msgps
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{dist}
Summary:          Calculates the degrees of freedom of elastic net, adaptive lasso and generalized elastic net

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package computes the degrees of freedom of the lasso, elastic net,
generalized elastic net and adaptive lasso based on the generalized path
seeking algorithm.  The optimal model can be selected by model selection
criteria including Mallows' Cp, bias-corrected AIC (AICc), generalized
cross validation (GCV) and BIC.

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
%doc %{rlibdir}/msgps/DESCRIPTION
%doc %{rlibdir}/msgps/html
%{rlibdir}/msgps/libs
%{rlibdir}/msgps/help
%{rlibdir}/msgps/NAMESPACE
%{rlibdir}/msgps/Meta
%{rlibdir}/msgps/INDEX
%{rlibdir}/msgps/R

%changelog
* Mon Feb 13 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- Update to version 1.1

* Sat Dec 03 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora