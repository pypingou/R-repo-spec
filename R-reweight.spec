%global packname  reweight
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.02
Release:          1%{?dist}
Summary:          Adjustment of Survey Respondent Weights

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Adjusts the weights of survey respondents so that the marginal
distributions of certain variables fit more closely to those from a more
precise source (e.g. Census Bureau's data).

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
%doc %{rlibdir}/reweight/doc
%doc %{rlibdir}/reweight/DESCRIPTION
%doc %{rlibdir}/reweight/html
%{rlibdir}/reweight/R
%{rlibdir}/reweight/INDEX
%{rlibdir}/reweight/NAMESPACE
%{rlibdir}/reweight/help
%{rlibdir}/reweight/Meta
%{rlibdir}/reweight/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.02-1
- initial package for Fedora