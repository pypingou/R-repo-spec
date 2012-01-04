%global packname  ecoreg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Ecological regression using aggregate and individual data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Estimating individual-level covariate-outcome associations using aggregate
data ("ecological inference") or a combination of aggregate and
individual-level data ("hierarchical related regression").

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
%doc %{rlibdir}/ecoreg/CITATION
%doc %{rlibdir}/ecoreg/doc
%doc %{rlibdir}/ecoreg/DESCRIPTION
%doc %{rlibdir}/ecoreg/html
%doc %{rlibdir}/ecoreg/NEWS
%{rlibdir}/ecoreg/NAMESPACE
%{rlibdir}/ecoreg/help
%{rlibdir}/ecoreg/R
%{rlibdir}/ecoreg/INDEX
%{rlibdir}/ecoreg/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora