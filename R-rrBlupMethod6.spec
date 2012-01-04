%global packname  rrBlupMethod6
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Re-parametrization of RR-BLUP to allow for a fixed residual variance

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
rrBlupMethod6 -- Re-parametrization of mixed model formulation to allow
for a fixed residual variance when using RR-BLUP for genomwide estimation
of marker effects.

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
%doc %{rlibdir}/rrBlupMethod6/CITATION
%doc %{rlibdir}/rrBlupMethod6/DESCRIPTION
%doc %{rlibdir}/rrBlupMethod6/html
%{rlibdir}/rrBlupMethod6/INDEX
%{rlibdir}/rrBlupMethod6/NAMESPACE
%{rlibdir}/rrBlupMethod6/help
%{rlibdir}/rrBlupMethod6/R
%{rlibdir}/rrBlupMethod6/Meta

%changelog
* Mon Dec 05 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora