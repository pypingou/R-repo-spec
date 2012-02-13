%global packname  cacIRT
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{dist}
Summary:          Computes classification accuracy and consistency under Item Response Theory

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Computes classification accuracy and consistency under Item Response
Theory by the approach proposed by Lee, Hanson & Brennen (2002) and Lee
(2010) or the approach proposed by Rudner (2001, 2005). [Currently, only
works for 3PL IRT models (or 2PL or 1PL) (future updates should include
polytomous models), and only independent cut scores (imputing multiple cut
scores will apply them independently but not simultaneously).]

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
%doc %{rlibdir}/cacIRT/DESCRIPTION
%doc %{rlibdir}/cacIRT/html
%{rlibdir}/cacIRT/NAMESPACE
%{rlibdir}/cacIRT/R
%{rlibdir}/cacIRT/Meta
%{rlibdir}/cacIRT/help
%{rlibdir}/cacIRT/INDEX

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- Update to version 1.1

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora