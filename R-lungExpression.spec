%global packname  lungExpression
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.12
Release:          1%{?dist}
Summary:          ExpressionSets for Parmigiani et al., 2004 Clinical Cancer Research paper

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Biobase 

BuildRequires:    R-devel tex(latex) R-Biobase 

%description
Data from three large lung cancer studies provided as ExpressionSets

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
%doc %{rlibdir}/lungExpression/html
%doc %{rlibdir}/lungExpression/DESCRIPTION
%{rlibdir}/lungExpression/Meta
%{rlibdir}/lungExpression/INDEX
%{rlibdir}/lungExpression/help
%{rlibdir}/lungExpression/data
%{rlibdir}/lungExpression/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.12-1
- initial package for Fedora