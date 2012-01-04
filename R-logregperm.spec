%global packname  logregperm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Inference in Logistic Regression

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A permutation test is used for inference in logistic regression. The
procedure is useful when parameter estimates in ordinary logistic
regression fail to converge or are unreliable due to small sample size, or
when the conditioning in exact conditional logistic regression restricts
the sample space too severely.

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
%doc %{rlibdir}/logregperm/DESCRIPTION
%doc %{rlibdir}/logregperm/html
%{rlibdir}/logregperm/Meta
%{rlibdir}/logregperm/INDEX
%{rlibdir}/logregperm/help
%{rlibdir}/logregperm/NAMESPACE
%{rlibdir}/logregperm/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora