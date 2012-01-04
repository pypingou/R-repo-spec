%global packname  glmperm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Inference in Generalized Linear Models

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A permutation test is used for inference in generalized linear models
(glm). The procedure is useful when parameter estimates in ordinary glm
fail to converge or are unreliable due to small sample size.

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
%doc %{rlibdir}/glmperm/DESCRIPTION
%doc %{rlibdir}/glmperm/html
%{rlibdir}/glmperm/NAMESPACE
%{rlibdir}/glmperm/INDEX
%{rlibdir}/glmperm/Meta
%{rlibdir}/glmperm/help
%{rlibdir}/glmperm/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora