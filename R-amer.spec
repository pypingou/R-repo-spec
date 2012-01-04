%global packname  amer
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.10
Release:          1%{?dist}
Summary:          Additive mixed models with lme4

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-nlme R-Matrix R-splines R-lme4 


BuildRequires:    R-devel tex(latex) R-methods R-nlme R-Matrix R-splines R-lme4



%description
Fitting generalized additive mixed models based on the mixed model
algorithm of lme4

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
%doc %{rlibdir}/amer/html
%doc %{rlibdir}/amer/CITATION
%doc %{rlibdir}/amer/doc
%doc %{rlibdir}/amer/DESCRIPTION
%{rlibdir}/amer/data
%{rlibdir}/amer/Meta
%{rlibdir}/amer/R
%{rlibdir}/amer/help
%{rlibdir}/amer/INDEX
%{rlibdir}/amer/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.10-1
- initial package for Fedora