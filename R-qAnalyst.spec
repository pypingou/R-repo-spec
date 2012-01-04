%global packname  qAnalyst
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.4
Release:          1%{?dist}
Summary:          Control Charts, Capability and Distribution Identification

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-MASS R-car R-SuppDists 


BuildRequires:    R-devel tex(latex) R-lattice R-MASS R-car R-SuppDists



%description
qAnalyst performs: control charts for variables and attributes according
to Douglas C. Montgomery Introduction to Statistical Quality Control book,
Capability analysis for normal and non - normal distributions and
Distributions Identification

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
%doc %{rlibdir}/qAnalyst/html
%doc %{rlibdir}/qAnalyst/DESCRIPTION
%doc %{rlibdir}/qAnalyst/doc
%{rlibdir}/qAnalyst/R
%{rlibdir}/qAnalyst/NAMESPACE
%{rlibdir}/qAnalyst/help
%{rlibdir}/qAnalyst/INDEX
%{rlibdir}/qAnalyst/demo
%{rlibdir}/qAnalyst/Meta
%{rlibdir}/qAnalyst/data

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.4-1
- initial package for Fedora