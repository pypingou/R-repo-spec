%global packname  LPEadj
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.14.0
Release:          1%{?dist}
Summary:          A correction of the local pooled error (LPE) method to replace the asymptotic variance adjustment with an unbiased adjustment based on sample size.

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-LPE 

BuildRequires:    R-devel tex(latex) R-LPE 

%description
Two options are added to the LPE algorithm. The original LPE method sets
all variances below the max variance in the ordered distribution of
variances to the maximum variance. in LPEadj this option is turned off by
default.  The second option is to use a variance adjustment based on
sample size rather than pi/2.  By default the LPEadj uses the sample size
based variance adjustment.

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
%doc %{rlibdir}/LPEadj/doc
%doc %{rlibdir}/LPEadj/DESCRIPTION
%doc %{rlibdir}/LPEadj/html
%{rlibdir}/LPEadj/R
%{rlibdir}/LPEadj/Meta
%{rlibdir}/LPEadj/help
%{rlibdir}/LPEadj/INDEX
%{rlibdir}/LPEadj/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.14.0-1
- initial package for Fedora