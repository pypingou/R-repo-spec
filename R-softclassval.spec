%global packname  softclassval
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.20110804
Release:          1%{?dist}
Summary:          Soft classification performance measures

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-20110804.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-svUnit R-methods R-arrayhelpers 


BuildRequires:    R-devel tex(latex) R-svUnit R-methods R-arrayhelpers



%description
Extension of sensitivity, specificity, positive and negative predictive
value to continuous predicted and reference memberships in [0, 1]

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.20110804-1
- initial package for Fedora