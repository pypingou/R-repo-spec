%global packname  hier.part
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Hierarchical Partitioning

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-gtools 

BuildRequires:    R-devel tex(latex) R-gtools 

%description
Variance partition of a multivariate data set

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
%doc %{rlibdir}/hier.part/html
%doc %{rlibdir}/hier.part/DESCRIPTION
%{rlibdir}/hier.part/libs
%{rlibdir}/hier.part/data
%{rlibdir}/hier.part/R
%{rlibdir}/hier.part/Meta
%{rlibdir}/hier.part/help
%{rlibdir}/hier.part/INDEX
%{rlibdir}/hier.part/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora