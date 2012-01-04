%global packname  profileModel
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.8
Release:          1%{?dist}
Summary:          Tools for profiling inference functions for various model classes

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
profileModel provides tools that can be used to calculate, evaluate, plot
and use for inference the profiles of *arbitrary* inference functions for
*arbitrary* 'glm'-like fitted models with linear predictors.

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
%doc %{rlibdir}/profileModel/html
%doc %{rlibdir}/profileModel/DESCRIPTION
%doc %{rlibdir}/profileModel/CITATION
%{rlibdir}/profileModel/R
%{rlibdir}/profileModel/Meta
%{rlibdir}/profileModel/NAMESPACE
%{rlibdir}/profileModel/CHANGES
%{rlibdir}/profileModel/help
%{rlibdir}/profileModel/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.8-1
- initial package for Fedora