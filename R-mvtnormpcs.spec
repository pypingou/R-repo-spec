%global packname  mvtnormpcs
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Multivariate Normal and T Distribution functions of (Dunnett, 1989)

Group:            Applications/Engineering 
License:          LGPL >= 2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Computes multivariate student and multivariate normal integrals, given a
correlation matrix structure defined by a vector bpd, s.t. rho(i,j) =
bpd(i) * bpd(j)   (product correlation structure)

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
%doc %{rlibdir}/mvtnormpcs/DESCRIPTION
%doc %{rlibdir}/mvtnormpcs/html
%{rlibdir}/mvtnormpcs/libs
%{rlibdir}/mvtnormpcs/R
%{rlibdir}/mvtnormpcs/help
%{rlibdir}/mvtnormpcs/INDEX
%{rlibdir}/mvtnormpcs/Meta
%{rlibdir}/mvtnormpcs/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora