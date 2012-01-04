%global packname  MLPAstats
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.9
Release:          1%{?dist}
Summary:          MLPA analysis to detect gains and loses in genes

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-nlme R-boot R-tcltk R-tkrplot R-pixmap 

BuildRequires:    R-devel tex(latex) R-nlme R-boot R-tcltk R-tkrplot R-pixmap 

%description
MLPAstats is a software designed to test copy number differences between
case and control samples, identified with multiplex-dependent probe
amplification (MLPA) data. The package incorporates several methods for
data normalization and copy number alterations such as REX-regression,
threshold approach and mixed-models.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.9-1
- initial package for Fedora